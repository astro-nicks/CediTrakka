"""
Cedi Trakka Intelligent Financial Tracking Agent
SPADE Implementation
DCIT 403 Designing Intelligent Agents
Author: Essandoh Astrea Kwame Jnr
"""

import json
import re
from datetime import datetime
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour, OneShotBehaviour
from spade.message import Message

# ------------------------------------------------------------
# Utility functions (parsing + classification)
# ------------------------------------------------------------

def parse_message(text):
    amount_pattern = r"GHS?\s?(\d+\.?\d*)"
    amount_match = re.search(amount_pattern, text)

    amount = float(amount_match.group(1)) if amount_match else 0.0

    if "sent" in text.lower():
        t_type = "debit"
    elif "received" in text.lower() or "credited" in text.lower():
        t_type = "credit"
    else:
        t_type = "unknown"

    return {
        "raw": text,
        "amount": amount,
        "type": t_type,
        "timestamp": datetime.now().isoformat()
    }


def classify_transaction(data):
    text = data["raw"].lower()
    amt = data["amount"]

    if "transfer" in text or "sent" in text:
        return "Transfers"
    if "airtime" in text:
        return "Airtime/Data"
    if amt < 20:
        return "Food"
    if "bill" in text or "utility" in text:
        return "Bills"
    return "Miscellaneous"

# ------------------------------------------------------------
# Main Agent Definition
# ------------------------------------------------------------

class CediTrakkaAgent(Agent):

    transaction_file = "transactions.json"

    def load_transactions(self):
        try:
            with open(self.transaction_file, "r") as f:
                return json.load(f)
        except:
            return []

    def save_transaction(self, tx):
        tx_list = self.load_transactions()
        tx_list.append(tx)
        with open(self.transaction_file, "w") as f:
            json.dump(tx_list, f, indent=4)

    # ------------------ BEHAVIOURS --------------------------

    class NotificationListener(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=3)

            if msg:
                print("\n--- NEW NOTIFICATION RECEIVED ---")
                print("Message:", msg.body)

                self.agent.message_to_parse = msg.body
                self.agent.add_behaviour(self.agent.ParseTransaction())

    class ParseTransaction(OneShotBehaviour):
        async def run(self):
            text = self.agent.message_to_parse
            parsed = parse_message(text)
            print("Parsed:", parsed)

            self.agent.current_parsed = parsed
            self.agent.add_behaviour(self.agent.ClassifyTransaction())

    class ClassifyTransaction(OneShotBehaviour):
        async def run(self):
            parsed = self.agent.current_parsed
            category = classify_transaction(parsed)

            parsed["category"] = category
            print("Classified as:", category)

            self.agent.save_transaction(parsed)
            self.agent.add_behaviour(self.agent.AnalyzeSpending())

    class AnalyzeSpending(OneShotBehaviour):
        async def run(self):
            data = self.agent.load_transactions()

            category_sums = {}
            for tx in data:
                cat = tx["category"]
                category_sums[cat] = category_sums.get(cat, 0) + tx["amount"]

            if category_sums.get("Food", 0) > 200:
                print("⚠️ ALERT: You are overspending on Food this week!")

            print("Updated spending totals:", category_sums)

    class MonthlySummary(PeriodicBehaviour):
        async def run(self):
            data = self.agent.load_transactions()
            if not data:
                return

            print("\n===== MONTHLY SUMMARY =====")
            totals = {}
            for tx in data:
                cat = tx["category"]
                totals[cat] = totals.get(cat, 0) + tx["amount"]

            for cat, total in totals.items():
                print(f"{cat}: GHS {total}")
            print("==========================\n")

    async def setup(self):
        print(f"[{self.jid}] Cedi Trakka Agent Started")
        self.add_behaviour(self.NotificationListener())
        self.add_behaviour(self.MonthlySummary(period=30))

# ------------------------------------------------------------
# SIMULATION DRIVER
# ------------------------------------------------------------

import asyncio

if __name__ == "__main__":

    async def main():
        agent_jid = "ceditrakka@xmpp.jp"
        agent_pw = "1234569"

        cedi_agent = CediTrakkaAgent(agent_jid, agent_pw)

        print("Starting agent...")
        await cedi_agent.start()

        # ✅ FIXED SIMULATION (no .send() needed)
        async def simulate_messages():
            await asyncio.sleep(5)

            sample_msgs = [
                "You sent GHS 50.00 to Ama.",
                "You received GHS 200.00 from Kojo.",
                "Airtime purchase of GHS 15 successful.",
                "Paid utility bill of GHS 120.",
                "You sent GHS 10.00 to Esi."
            ]

            for m in sample_msgs:
                print("\n--- SIMULATED NOTIFICATION ---")
                print(m)

                # Directly trigger the behaviour
                cedi_agent.message_to_parse = m
                cedi_agent.add_behaviour(cedi_agent.ParseTransaction())

                await asyncio.sleep(4)

        asyncio.create_task(simulate_messages())

        # Keep agent running
        while cedi_agent.is_alive():
            try:
                await asyncio.sleep(1)
            except KeyboardInterrupt:
                break

        await cedi_agent.stop()
        print("Agent stopped.")

    asyncio.run(main())