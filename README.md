# Meridian AWS Cloud Services — Streamlit E-Portfolio

A two-section academic portfolio based on the supplied Meridian AWS Cloud Subscription Model workbook and AS3 presentation.

## Features
- **Problem:** business context, revenue mix, workforce planning challenge, Tesco benchmark cross-check and key risks.
- **Solution:** service model, employee lifecycle, role accountability, manpower calculations, cost structure and projected P&L.
- **Calculations & Data:** formulas, assumptions and source limitations.
- Interactive Plotly charts and expandable calculation explanations.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Streamlit:

   ```bash
   streamlit run app.py
   ```

## Upload to GitHub
1. Create a new GitHub repository, for example `meridian-aws-eportfolio`.
2. Upload `app.py`, `requirements.txt`, and `README.md` to the repository root.
3. Commit the files.

## Deploy on Streamlit Community Cloud
1. Sign in to Streamlit Community Cloud using your GitHub account.
2. Choose **Create app**.
3. Select your repository and branch.
4. Set the main file path to `app.py`.
5. Deploy.

## Important modelling notes
- The ₹100 crore annual revenue ambition is a steady-state planning assumption, not a guaranteed first-year forecast.
- Revenue is modelled as 200 cloud subscriptions × ₹20 lakh, 50 security contracts × ₹50 lakh, and 70 engineering projects/retainers × ₹50 lakh.
- The 153-person plan is a benchmark-based planning estimate, not actual Meridian headcount or confirmed vacancies.
- The Tesco benchmark is a separate cross-check. Do not add Tesco cost ratios to the bottom-up Meridian operating-cost model.
- Manpower benefits (18%), hiring/onboarding/training reserve (5%), depreciation (₹3 crore), interest (₹1 crore), and tax (25% of PBT) are illustrative assumptions.
- Confirm pricing authority, AWS partner/reseller permissions, customer billing treatment, vendor costs and salary assumptions before treating the model as an operating forecast.
