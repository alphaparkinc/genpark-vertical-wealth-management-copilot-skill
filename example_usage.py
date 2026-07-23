from client import VerticalWealthManagementCopilotClient

def main():
    client = VerticalWealthManagementCopilotClient()
    res = client.analyze_portfolio(
        client_id="client_8801",
        portfolio_holdings=[
            {"ticker": "NVDA", "type": "equity", "value_usd": 450000},
            {"ticker": "AAPL", "type": "equity", "value_usd": 300000},
            {"ticker": "BND", "type": "bond", "value_usd": 150000}
        ]
    )
    print(f"Risk Assessment: {res['risk_assessment']}")
    print(f"Allocation: {res['asset_allocation']}")
    print("Rebalance Actions:")
    for act in res["recommended_rebalance"]:
        print(f"  - {act}")

if __name__ == "__main__":
    main()
