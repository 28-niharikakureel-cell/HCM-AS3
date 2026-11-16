import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------
# MERIDIAN | AWS CLOUD SERVICES - E-PORTFOLIO
# Source: uploaded Meridian AWS Cloud Subscription Model workbook
#         and Meridian AS3 presentation.
# All financial values are illustrative planning assumptions.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Meridian | AWS Cloud Services Portfolio",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Pastel palette
PURPLE = "#A88DBB"
PINK = "#E7B0A8"
GREEN = "#AFC7B2"
YELLOW = "#E8D69B"
DARK = "#30343B"
LIGHT_BG = "#F8F7F5"

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {LIGHT_BG}; }}
    [data-testid="stSidebar"] {{ background-color: #F0EAF4; }}
    h1, h2, h3 {{ color: {DARK}; }}
    .hero {{
        background: linear-gradient(110deg, #EDE5F2, #F6E8E5, #E7F0E8);
        padding: 1.6rem 1.8rem;
        border-radius: 18px;
        border: 1px solid #E4DDE6;
        margin-bottom: 1rem;
    }}
    .small-note {{ color: #666; font-size: 0.88rem; }}
    .section-card {{
        background: white;
        border: 1px solid #E7E2E8;
        border-radius: 14px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }}
    div[data-testid="stMetric"] {{
        background: white;
        border: 1px solid #E9E3EA;
        padding: 12px 14px;
        border-radius: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------- SOURCE DATA -------------------------
revenue = pd.DataFrame({
    "Revenue stream": [
        "AWS cloud platform subscriptions",
        "Managed network-security add-ons",
        "On-demand engineering services",
    ],
    "Contracts / projects": [200, 50, 70],
    "Average annual value (₹ crore)": [0.20, 0.50, 0.50],
    "Revenue (₹ crore)": [40.0, 25.0, 35.0],
    "Revenue type": ["Recurring", "Recurring add-on", "Project / retainer"],
})

workforce = pd.DataFrame({
    "Function": [
        "Cloud Engineers",
        "Software Developers",
        "Operations & Customer Support",
        "Sales & Business Development",
        "Marketing",
        "Finance",
        "HR & Administration",
    ],
    "Employees": [55, 35, 30, 15, 7, 5, 6],
    "Average annual CTC (₹ lakh)": [21.0, 19.5, 12.0, 16.0, 13.0, 14.0, 11.0],
})
workforce["Annual salary cost (₹ crore)"] = (
    workforce["Employees"] * workforce["Average annual CTC (₹ lakh)"] / 100
)

# Workbook manpower plan
fixed_salary = 26.645
benefits_rate = 0.18
training_rate = 0.05
benefits_cost = fixed_salary * benefits_rate
training_cost = fixed_salary * training_rate
manpower_cost = fixed_salary + benefits_cost + training_cost

costs = pd.DataFrame({
    "Cost category": [
        "Manpower",
        "Cloud, software, security & engineering",
        "Sales & marketing",
        "Administration & contingency",
    ],
    "Annual cost (₹ crore)": [manpower_cost, 8.6, 7.1, 4.7],
})
total_revenue = float(revenue["Revenue (₹ crore)"].sum())
total_opex = float(costs["Annual cost (₹ crore)"].sum())
ebitda = total_revenue - total_opex
depreciation = 3.0
ebit = ebitda - depreciation
interest = 1.0
pbt = ebit - interest
tax_rate = 0.25
tax = pbt * tax_rate
pat = pbt - tax
ebitda_margin = ebitda / total_revenue
pat_margin = pat / total_revenue

# Separate Tesco benchmark cross-check from workbook
tesco_revenue = 2613.1
tesco_workforce = 4000
tesco_revenue_per_employee = tesco_revenue / tesco_workforce
tesco_headcount_equivalent = 100 / tesco_revenue_per_employee
tesco_employee_cost_ratio = 0.6045
tesco_other_cost_ratio = 0.2402
tesco_operating_profit_ratio = 0.1553

# ------------------------- HELPERS -------------------------
def section_heading(kicker, title, description=None):
    st.caption(kicker.upper())
    st.subheader(title)
    if description:
        st.write(description)

def money(value):
    return f"₹{value:,.2f} Cr"

def metric_row():
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Annual revenue ambition", "₹100 Cr")
    c2.metric("Planned workforce", "153")
    c3.metric("Operating expenses", money(total_opex))
    c4.metric("Illustrative EBITDA", money(ebitda))

def show_calculation(label, formula, result, explanation):
    with st.expander(label, expanded=False):
        st.code(formula, language="text")
        st.markdown(f"**Result: {result}**")
        st.write(explanation)

# ------------------------- HEADER / NAVIGATION -------------------------
with st.sidebar:
    st.title("☁️ Meridian Portfolio")
    st.caption("AWS Cloud Subscription & Services")
    page = st.radio(
        "Navigate portfolio",
        ["Overview", "01 · Problem", "02 · Solution", "Calculations & Data"],
        index=0,
    )
    st.divider()
    st.caption("Prepared from the supplied Excel model and AS3 presentation.")
    st.caption("Figures are illustrative planning assumptions.")

st.markdown(
    """
    <div class="hero">
      <h1 style="margin:0;">MERIDIAN | AWS CLOUD SERVICES</h1>
      <p style="font-size:1.08rem;margin:.45rem 0 0 0;">
        Business problem, financial analysis and proposed people solution
      </p>
      <p class="small-note" style="margin:.5rem 0 0 0;">
        E-portfolio · Strategy · Workforce planning · Financial modelling
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------- OVERVIEW -------------------------
if page == "Overview":
    st.title("Project at a glance")
    st.write(
        "This portfolio presents a proposed subscription-led AWS cloud services "
        "business for Meridian. AWS is the underlying cloud provider; Meridian's "
        "proposed role is to manage onboarding, cloud operations, customer support, "
        "security add-ons and optional engineering work."
    )
    metric_row()

    st.markdown("### Business model")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### ☁️ Cloud subscription")
        st.write("Managed AWS environment, onboarding, monitoring, backup, support and usage visibility.")
        st.caption("Recurring monthly or annual fee")
    with c2:
        st.markdown("#### 🛡️ Network security")
        st.write("Access controls, firewall/WAF configuration, monitoring and vulnerability checks.")
        st.caption("Optional recurring add-on")
    with c3:
        st.markdown("#### 🧑‍💻 Engineering")
        st.write("Custom software, APIs, integrations, cloud migration, DevOps and automation.")
        st.caption("Project or retainer income")

    st.markdown("### Revenue ambition")
    fig = px.bar(
        revenue, x="Revenue stream", y="Revenue (₹ crore)",
        color="Revenue stream",
        color_discrete_sequence=[PURPLE, PINK, GREEN],
        text="Revenue (₹ crore)",
    )
    fig.update_layout(showlegend=False, yaxis_title="₹ crore", xaxis_title="", plot_bgcolor="white")
    fig.update_traces(texttemplate="₹%{text:.0f} Cr", textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Important assumption: ₹100 crore is an illustrative steady-state annual "
        "target, not a guaranteed first-year forecast. Contract volumes, average "
        "values, pricing authority and AWS customer-usage billing need validation."
    )

# ------------------------- PROBLEM -------------------------
elif page == "01 · Problem":
    st.title("01 | The business problem")
    st.write(
        "Meridian's proposed AWS service model needs to turn a revenue ambition "
        "into a deliverable operating model. The challenge is not only how many "
        "people to hire, but whether the business has the right capability, "
        "coverage, authority and cost structure."
    )

    section_heading(
        "Business context",
        "A ₹100 crore ambition with three different revenue streams",
        "The model combines recurring subscription income with project-based engineering income.",
    )
    metric_row()

    fig_rev = px.pie(
        revenue, names="Revenue stream", values="Revenue (₹ crore)",
        hole=0.48, color_discrete_sequence=[PURPLE, PINK, GREEN],
    )
    fig_rev.update_traces(textposition="inside", textinfo="label+percent")
    fig_rev.update_layout(margin=dict(t=15, b=15, l=10, r=10))
    st.plotly_chart(fig_rev, use_container_width=True)

    st.markdown("#### Revenue calculation")
    rev_table = revenue.copy()
    rev_table["Average annual value (₹ lakh)"] = rev_table["Average annual value (₹ crore)"] * 100
    st.dataframe(
        rev_table[["Revenue stream", "Contracts / projects", "Average annual value (₹ lakh)", "Revenue (₹ crore)", "Revenue type"]],
        use_container_width=True, hide_index=True,
    )
    show_calculation(
        "How the ₹100 crore target is built",
        "Cloud subscriptions: 200 × ₹0.20 Cr = ₹40 Cr\n"
        "Security contracts: 50 × ₹0.50 Cr = ₹25 Cr\n"
        "Engineering projects/retainers: 70 × ₹0.50 Cr = ₹35 Cr\n"
        "Total revenue = ₹40 Cr + ₹25 Cr + ₹35 Cr",
        "₹100 crore",
        "The platform and security lines are recurring in the model. Engineering is project or retainer income when customers need additional work.",
    )

    st.divider()
    section_heading(
        "Workforce challenge",
        "Headcount does not automatically create capability",
        "The workbook proposes 153 employees across seven functions. The AS3 presentation focuses on 55 planned Cloud Engineering roles, with an indicative average annual CTC of ₹21 lakh.",
    )
    left, right = st.columns([1.05, 1])
    with left:
        fig_people = px.bar(
            workforce.sort_values("Employees", ascending=True),
            x="Employees", y="Function", orientation="h",
            color="Function",
            color_discrete_sequence=[PURPLE, PINK, GREEN, YELLOW, "#C8B6D8", "#D8C5B8", "#B9C9D8"],
            text="Employees",
        )
        fig_people.update_layout(showlegend=False, xaxis_title="Number of employees", yaxis_title="", plot_bgcolor="white")
        st.plotly_chart(fig_people, use_container_width=True)
    with right:
        st.markdown("#### What must be solved")
        st.markdown(
            "- **Skills:** AWS, troubleshooting, security and risk judgement.\n"
            "- **Time:** enough coverage for monitoring and incident response.\n"
            "- **Access:** secure permissions and tools to perform the role.\n"
            "- **Authority:** clarity on who can contract, price and bill customers.\n"
            "- **Readiness:** practical evidence that employees can deliver the service."
        )
        st.metric("Cloud Engineering roles", "55")
        st.metric("Indicative average annual CTC", "₹21 lakh")

    show_calculation(
        "How the 153-person workforce was cross-checked",
        "Tesco revenue per colleague = ₹2,613.1 Cr ÷ 4,000\n"
        "= ₹0.653275 Cr per colleague\n"
        "Meridian benchmark headcount = ₹100 Cr ÷ ₹0.653275 Cr",
        f"Approximately {tesco_headcount_equivalent:.0f} employees",
        "This is a productivity benchmark cross-check only. The 153-person plan is not actual Meridian headcount or confirmed vacancies. The workbook says to validate workload, service coverage and skills before hiring.",
    )

    st.divider()
    section_heading(
        "Financial challenge",
        "Separate a benchmark from the bottom-up operating plan",
        "The workbook retains Tesco cost ratios as a separate comparison. The main Meridian financial view is calculated bottom-up from its manpower plan and operating-cost assumptions.",
    )
    benchmark = pd.DataFrame({
        "Tesco benchmark applied to ₹100 Cr": ["Employee costs", "Other operating expenses", "Operating profit"],
        "Share of revenue": [60.45, 24.02, 15.53],
        "Amount (₹ crore)": [60.45, 24.02, 15.53],
    })
    st.dataframe(benchmark, use_container_width=True, hide_index=True)
    st.warning(
        "Do not add Tesco benchmark costs to Meridian's detailed cost sheet. "
        "They are two separate views and serve different purposes."
    )

    st.markdown("### Key risks identified in the workbook")
    risk_cols = st.columns(2)
    risks = [
        ("Commercial authority / AWS route", "Confirm parent approval, AWS partner permissions, pricing authority, customer contracts and billing route."),
        ("Data privacy and security", "Use least-privilege access, encryption, network segmentation, monitoring and incident procedures."),
        ("Cloud availability and SLA failure", "Define service levels, backup, recovery, escalation and service ownership."),
        ("Customer adoption and trust", "Use scoped pilots, transparent packages, usage reporting and responsive support."),
        ("Engineering overruns", "Use discovery, clear scope, milestones and change control."),
        ("Talent and capability gaps", "Map KSAB to roles, use practical assessments and provide AWS/security training."),
    ]
    for i, (name, action) in enumerate(risks):
        with risk_cols[i % 2]:
            st.markdown(f'<div class="section-card"><b>{name}</b><br>{action}</div>', unsafe_allow_html=True)

# ------------------------- SOLUTION -------------------------
elif page == "02 · Solution":
    st.title("02 | The proposed solution")
    st.write(
        "The solution is to build the business around three connected elements: "
        "a clear service and revenue model, a validated workforce plan, and an "
        "employee lifecycle that develops and retains practical capability."
    )

    section_heading("Business solution", "Three service lines support the ₹100 crore plan")
    st.dataframe(revenue, use_container_width=True, hide_index=True)
    fig = px.bar(
        revenue, x="Revenue stream", y="Revenue (₹ crore)",
        color="Revenue stream", color_discrete_sequence=[PURPLE, PINK, GREEN],
        text="Revenue (₹ crore)",
    )
    fig.update_layout(showlegend=False, plot_bgcolor="white", xaxis_title="", yaxis_title="₹ crore")
    fig.update_traces(texttemplate="₹%{text:.0f} Cr", textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    section_heading(
        "People solution",
        "Build capability through the employee lifecycle",
        "The AS3 proposal moves beyond recruitment: it links selection, onboarding, performance, growth and retention to service outcomes.",
    )
    lifecycle = [
        ("1. Attract & Select", "Set clear role criteria. Assess AWS knowledge, troubleshooting and risk judgement."),
        ("2. Onboard & Practise", "Provide secure access, service context, mentoring and supervised incident exercises."),
        ("3. Perform", "Use 30/60/90-day reviews. Balance SLA, quality, security and customer outcomes."),
        ("4. Grow", "Enable applied learning and fair access to architecture, security, DevOps and FinOps work."),
        ("5. Retain", "Use transparent rewards, employee voice, wellbeing checks and recovery time after global calls."),
    ]
    for title, desc in lifecycle:
        st.markdown(
            f'<div class="section-card"><b>{title}</b><br>{desc}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("### Role accountability and evidence of performance")
    accountability = pd.DataFrame({
        "Role accountability": [
            "Cloud availability",
            "Incident response",
            "Security and access",
            "Recovery and cost",
        ],
        "Evidence / KPI": [
            "Uptime and SLA achievement",
            "Resolution time and repeat incidents",
            "Findings closed; access compliance",
            "Backup success; cloud-cost variance",
        ],
    })
    st.dataframe(accountability, use_container_width=True, hide_index=True)

    st.divider()
    section_heading("Financial solution", "Calculate the cost and profit impact")
    st.write("The bottom-up plan combines the manpower estimate with cloud/engineering, sales/marketing and administration costs.")
    cost_col, chart_col = st.columns([1, 1.1])
    with cost_col:
        st.dataframe(costs, use_container_width=True, hide_index=True)
        st.markdown(f"**Total operating expenses: {money(total_opex)}**")
    with chart_col:
        fig_cost = px.pie(
            costs, names="Cost category", values="Annual cost (₹ crore)",
            hole=0.45, color_discrete_sequence=[PURPLE, PINK, GREEN, YELLOW],
        )
        fig_cost.update_traces(textinfo="label+percent")
        st.plotly_chart(fig_cost, use_container_width=True)

    show_calculation(
        "Manpower cost calculation",
        "Fixed salary / CTC = ₹26.645 Cr\n"
        "Benefits = ₹26.645 Cr × 18% = ₹4.7961 Cr\n"
        "Hiring, onboarding & training = ₹26.645 Cr × 5% = ₹1.33225 Cr\n"
        "Total manpower cost = 26.645 + 4.7961 + 1.33225",
        money(manpower_cost),
        "The 18% benefits and 5% hiring/training reserves are assumptions from the workbook, not verified HR quotations.",
    )
    show_calculation(
        "Operating expense calculation",
        "Manpower = ₹32.77335 Cr\n"
        "Cloud, software, security & engineering = ₹8.60 Cr\n"
        "Sales & marketing = ₹7.10 Cr\n"
        "Administration & contingency = ₹4.70 Cr\n"
        "Total operating expenses = sum of the four categories",
        money(total_opex),
        "The cost sheet describes these as illustrative estimates that need vendor quotations and internal validation.",
    )

    st.markdown("### Projected profit and loss")
    pnl = pd.DataFrame({
        "Financial measure": [
            "Revenue", "Operating expenses", "EBITDA",
            "Depreciation & amortisation", "EBIT", "Interest expense",
            "Profit before tax", "Tax provision", "Profit after tax",
        ],
        "Amount (₹ crore)": [
            total_revenue, total_opex, ebitda, depreciation,
            ebit, interest, pbt, tax, pat,
        ],
    })
    st.dataframe(pnl, use_container_width=True, hide_index=True)
    fig_pnl = go.Figure()
    fig_pnl.add_trace(go.Bar(
        x=["Revenue", "Operating expenses", "EBITDA", "EBIT", "Profit after tax"],
        y=[total_revenue, total_opex, ebitda, ebit, pat],
        marker_color=[PURPLE, PINK, GREEN, YELLOW, "#B9C9D8"],
        text=[f"₹{x:.2f} Cr" for x in [total_revenue, total_opex, ebitda, ebit, pat]],
        textposition="outside",
    ))
    fig_pnl.update_layout(
        yaxis_title="₹ crore", xaxis_title="", plot_bgcolor="white",
        title="Illustrative annual financial outcome",
    )
    st.plotly_chart(fig_pnl, use_container_width=True)

    show_calculation(
        "EBITDA and margin",
        "EBITDA = Revenue − Operating expenses\n"
        "= ₹100 Cr − ₹53.17335 Cr\n"
        "EBITDA margin = EBITDA ÷ Revenue × 100",
        f"{money(ebitda)} EBITDA | {ebitda_margin:.2%} margin",
        "EBITDA is the operating surplus before depreciation, interest and tax.",
    )
    show_calculation(
        "Profit after tax",
        "EBIT = EBITDA − Depreciation\n"
        "PBT = EBIT − Interest\n"
        "Tax = PBT × 25%\n"
        "PAT = PBT − Tax",
        f"{money(pat)} PAT | {pat_margin:.2%} PAT margin",
        "The 25% tax provision, ₹3 crore depreciation and ₹1 crore interest are illustrative workbook assumptions. Actual tax and financing costs may differ.",
    )

    st.success(
        "Recommended next step: validate customer demand, commercial authority, "
        "AWS billing treatment, vendor costs and role readiness before committing "
        "to the full hiring plan."
    )

# ------------------------- CALCULATIONS & DATA -------------------------
elif page == "Calculations & Data":
    st.title("Calculations & source data")
    st.write(
        "This section makes the main assumptions and formulas transparent so "
        "the calculations can be explained during evaluation."
    )

    st.markdown("### 1. Revenue model")
    st.dataframe(revenue, use_container_width=True, hide_index=True)
    st.latex(r"\text{Revenue} = \text{Number of contracts} \times \text{Average annual contract value}")
    st.markdown(
        f"- Cloud: 200 × ₹0.20 Cr = **₹40 Cr**\n"
        f"- Security: 50 × ₹0.50 Cr = **₹25 Cr**\n"
        f"- Engineering: 70 × ₹0.50 Cr = **₹35 Cr**\n"
        f"- Total: **₹{total_revenue:.2f} Cr**"
    )

    st.markdown("### 2. Workforce and salary model")
    st.dataframe(workforce, use_container_width=True, hide_index=True)
    st.markdown(
        f"Total planned employees = **{int(workforce['Employees'].sum())}** across seven functions.\n\n"
        f"Fixed annual salary cost = **₹{fixed_salary:.3f} Cr**.\n\n"
        f"Total manpower cost = fixed salary + 18% benefits + 5% hiring/training "
        f"= **₹{manpower_cost:.5f} Cr**."
    )

    st.markdown("### 3. Operating cost and profit")
    st.dataframe(costs, use_container_width=True, hide_index=True)
    st.markdown(
        f"- Operating expenses = **₹{total_opex:.5f} Cr**\n"
        f"- EBITDA = ₹100 Cr − ₹{total_opex:.5f} Cr = **₹{ebitda:.5f} Cr**\n"
        f"- EBITDA margin = ₹{ebitda:.5f} Cr ÷ ₹100 Cr × 100 = **{ebitda_margin:.2%}**\n"
        f"- Profit after tax = **₹{pat:.5f} Cr**"
    )

    st.markdown("### 4. Tesco benchmark cross-check")
    st.write(
        f"Tesco revenue per colleague = ₹{tesco_revenue:.1f} Cr ÷ "
        f"{tesco_workforce:,} = ₹{tesco_revenue_per_employee:.6f} Cr."
    )
    st.write(
        f"Indicative Meridian workforce equivalent = ₹100 Cr ÷ "
        f"₹{tesco_revenue_per_employee:.6f} Cr = **{tesco_headcount_equivalent:.1f}, "
        f"approximately 153 employees**."
    )
    st.caption(
        "This is a benchmark-only cross-check, not actual Meridian staffing data. "
        "Tesco cost ratios are not added to the bottom-up Meridian cost model."
    )

    st.markdown("### Source and limitations")
    st.write(
        "Source documents: Meridian AWS Cloud Subscription Model – Updated "
        "(Excel workbook), and Meridian AS3 presentation. The portfolio preserves "
        "the workbook's distinction between the Tesco benchmark and the bottom-up "
        "Meridian financial plan."
    )
    st.warning(
        "All revenue, headcount, salary, operating-cost and profit figures are "
        "illustrative assumptions from the supplied model. The model itself "
        "requires validation of customer demand, pricing/contract authority, "
        "AWS partner permissions, AWS usage billing, vendor quotations and "
        "actual HR salary bands."
    )

st.divider()
st.caption(
    "Meridian AWS Cloud Subscription & Services | Academic e-portfolio | "
    "Figures are illustrative planning assumptions, not audited results."
)
