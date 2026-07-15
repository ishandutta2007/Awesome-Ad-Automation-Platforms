import os

os.makedirs('assets', exist_ok=True)

svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1a2a6c;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#b21f1f;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fdbb2d;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)">
    <animate attributeName="opacity" values="0.8;1;0.8" dur="3s" repeatCount="indefinite"/>
  </rect>
  <text x="50%" y="40%" dominant-baseline="middle" text-anchor="middle" fill="white" font-family="Arial, sans-serif" font-size="36" font-weight="bold">
    Awesome Ad Automation Platforms
    <animate attributeName="y" values="40%;45%;40%" dur="2s" repeatCount="indefinite"/>
  </text>
  <text x="50%" y="65%" dominant-baseline="middle" text-anchor="middle" fill="#eee" font-family="Arial, sans-serif" font-size="18">
    🚀 Top SaaS &amp; Open-Source Alternatives for E-Commerce Advertising
  </text>
</svg>"""

with open('assets/banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

readme_content = """# 🌟 Awesome Ad Automation Platforms

<p align="center">
  <img src="assets/banner.svg" alt="Awesome Ad Automation Platforms Banner" width="100%" />
</p>

<p align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
<a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

## 🚀 Top Ad Automation Platforms & Open-Source Alternatives

A curated guide to leading **SaaS/cloud-hosted Ad Automation Platforms** and their **open-source/self-hosted equivalents**. 

**Open-source solutions are emphasized** for customization, cost savings, and building your own ad management and optimization tools. Optimize your PPC, marketplace, and e-commerce advertising with AI bidding, campaign management, and performance tracking.

---

## 🏢 SaaS / Cloud-Hosted Ad Automation Platforms

Popular platforms for automating PPC, marketplace, and e-commerce advertising with AI bidding, campaign management, and performance optimization.

### 🌟 Leading Options

| Platform | Description | Pricing | Free Tier Limit | Company Size / Valuation |
|----------|-------------|---------|-----------------|--------------------------|
| **[Skai (Formerly Kenshoo)](https://skai.io)** | Enterprise search and social ad management. | Custom / Enterprise | No free tier | ~$1B Valuation |
| **[Pacvue](https://pacvue.com)** | Retail media and marketplace advertising platform. | Custom / Enterprise | No free tier | ~$1B Valuation |
| **[Quartile](https://quartile.com)** | AI-driven Amazon/marketplace ad optimization. | Custom (Quote-based) | No free tier | ~$500M Valuation |
| **[Feedonomics](https://feedonomics.com)** | Feed management and multi-channel ad optimization. | Custom | No free tier | ~$500M Valuation |
| **[Perpetua](https://perpetua.io)** | Automated bidding and campaign management. | Starts ~$250/mo + % of ad spend | No free tier | ~$100M Valuation |
| **[Teikametrics](https://teikametrics.com)** | Multi-channel ad optimization. | Free / % of ad spend | Free for sellers <$10k/mo revenue | ~$50M Valuation |
| **[Channable](https://channable.com)** | Feed management and multi-channel ad optimization. | Starts ~$39/mo | No free tier (Free Trial available) | ~$50M Valuation |
| **[Adspert](https://adspert.com)** | Automated bidding and campaign management. | Custom | No free tier | ~$20M Valuation |
| **[Adzooma](https://adzooma.com)** | Amazon and Google Ads automation. | Freemium / Paid plans | Essential features free for 1 account | ~$10M Valuation |
| **[Buy Box Experts](https://buyboxexperts.com)** | Amazon and Google Ads automation agency. | Custom | No free tier | Acquired by Pattern |
| **[Laurence](https://laurence.com)** | AI-driven Amazon/marketplace ad optimization. | Custom | No free tier | ~$1M Valuation |

These tools use AI for bid management, keyword optimization, and cross-platform campaign scaling.

---

## 🛠️ Open-Source / Self-Hosted Alternatives

Open-source options focus on custom scripts, self-hosted dashboards, and automation frameworks for ad data processing and optimization.

### 🌟 Featured Projects

| Project | Description | GitHub Stars |
|---------|-------------|--------------|
| **[Apache Superset](https://github.com/apache/superset)** | Self-hosted BI for ad performance visualization and alerting. | [![GitHub stars](https://img.shields.io/github/stars/apache/superset?style=social&color=white)](https://github.com/apache/superset/stargazers) |
| **[Metabase](https://github.com/metabase/metabase)** | Self-hosted BI for ad performance visualization and alerting. | [![GitHub stars](https://img.shields.io/github/stars/metabase/metabase?style=social&color=white)](https://github.com/metabase/metabase/stargazers) |
| **[Apache Airflow](https://github.com/apache/airflow)** | Orchestrating ad campaign workflows and reporting. | [![GitHub stars](https://img.shields.io/github/stars/apache/airflow?style=social&color=white)](https://github.com/apache/airflow/stargazers) |
| **[Airbyte](https://github.com/airbytehq/airbyte)** | Open-source data integration for pulling ad platform data. | [![GitHub stars](https://img.shields.io/github/stars/airbytehq/airbyte?style=social&color=white)](https://github.com/airbytehq/airbyte/stargazers) |
| **[dbt Core](https://github.com/dbt-labs/dbt-core)** | Transforming raw ad data into actionable insights. | [![GitHub stars](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=social&color=white)](https://github.com/dbt-labs/dbt-core/stargazers) |
| **[Great Expectations](https://github.com/great-expectations/great_expectations)** | Data quality in ad reporting pipelines. | [![GitHub stars](https://img.shields.io/github/stars/great-expectations/great_expectations?style=social&color=white)](https://github.com/great-expectations/great_expectations/stargazers) |
| **[Meltano](https://github.com/meltano/meltano)** | Open-source data integration for pulling ad platform data. | [![GitHub stars](https://img.shields.io/github/stars/meltano/meltano?style=social&color=white)](https://github.com/meltano/meltano/stargazers) |

### 🔧 Additional Open-Source Tools
- **Custom Python + Google Ads / Meta APIs** — Build tailored automation using official open APIs and libraries.
- Scripts and libraries for bid optimization, A/B testing, and feed generation (search GitHub for "ppc automation", "amazon ads api").
- **Open-source feed managers** and ETL tools for marketplace advertising.

**💡 Tip**: Combine **Airflow**, **dbt**, and API clients to create a powerful open ad automation stack. Use ML libraries (scikit-learn, Prophet) for custom bidding models.

---

## 📊 Comparison

| Aspect              | 🏢 SaaS Platforms                        | 🛠️ Open-Source / Self-Hosted                  |
|---------------------|---------------------------------------|--------------------------------------------|
| **Cost**            | Subscription + % of spend             | Free (infra + dev time)                    |
| **Customization**   | Platform rules                        | Full logic and algorithm control           |
| **Data Ownership**  | Vendor access                         | Complete control                           |
| **Setup Effort**    | Quick onboarding                      | Requires engineering                       |
| **Use Case**        | Agencies and brands wanting managed AI| Technical teams building custom solutions  |

---

## 🚀 Getting Started

1. Identify key platforms (Google, Amazon, Meta, etc.).
2. Use official APIs and **Airflow** for orchestration.
3. Build reporting with **Superset** and transformations with **dbt**.
4. Add ML for bidding/optimization as needed.
5. Deploy securely and monitor performance.

## 🤝 Contributing

Feel free to submit PRs to expand this list with more projects, tools, or comparisons!

**Last updated**: July 2026  
*Ad platforms change APIs frequently — always test automations thoroughly.*

## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Ad-Automation-Platforms&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Automation-Platforms&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Automation-Platforms&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Ad-Automation-Platforms&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)
