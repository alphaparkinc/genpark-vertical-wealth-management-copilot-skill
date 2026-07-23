class VerticalWealthManagementCopilotClient:
    def analyze_portfolio(self, client_id: str, portfolio_holdings: list) -> dict:
        total_val = sum(h.get("value_usd", 0) for h in portfolio_holdings)
        equity_val = sum(h.get("value_usd", 0) for h in portfolio_holdings if h.get("type") == "equity")
        bond_val = sum(h.get("value_usd", 0) for h in portfolio_holdings if h.get("type") == "bond")

        equity_pct = round(equity_val / max(total_val, 1) * 100, 1)
        bond_pct = round(bond_val / max(total_val, 1) * 100, 1)

        risk = "MODERATE_HIGH" if equity_pct > 70 else "BALANCED"
        rebalance = [
            f"Reduce equity exposure by {equity_pct - 60:.1f}% to align with 60/40 benchmark",
            "Reinvest dividends into Treasury inflation-protected securities"
        ] if equity_pct > 65 else ["Portfolio is optimally balanced"]

        return {
            "asset_allocation": {"equity_pct": equity_pct, "bond_pct": bond_pct, "total_value_usd": total_val},
            "risk_assessment": risk,
            "recommended_rebalance": rebalance
        }
