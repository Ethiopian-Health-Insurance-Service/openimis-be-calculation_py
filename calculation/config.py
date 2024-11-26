CLASS_RULE_PARAM_VALIDATION = [
    {
        "class": "ContributionPlan",
        "parameters": [
           {
                "type": "number",
                "name": "rate_employer_public",
                "label": {
                    "en": "Employer's percentage in Public Sector",
                    "fr": "Pourcentage de l'employeur dans le secteur public"
                },
                "rights": {
                    "read": "150201",
                    "write": "150202",
                    "update": "150203",
                    "replace": "150206",
                },
                "relevance": "True",
                "default": "0",
                "min": "0",
                "max": "100"
            },
            {
                "type": "number",
                "name": "rate_employer_private",
                "label": {
                    "en": "Employer's percentage in Private Sector",
                    "fr": "Pourcentage de l'employeur dans le secteur privé"
                },
                "rights": {
                    "read": "150201",
                    "write": "150202",
                    "update": "150203",
                    "replace": "150206",
                },
                "relevance": "True",
                "default": "0",
                "min": "0",
                "max": "100"
            },
            {
                "type": "number",
                "name": "rate_employee_public",
                "label": {
                    "en": "Employee's contribution percentage in the Public Sector",
                    "fr": "Pourcentage de l'employé dans le secteur public"
                },
                "rights": {
                    "read": "150201",
                    "write": "150202",
                    "update": "150203",
                    "replace": "150206",
                },
                "relevance": "True",
                "default": "0",
                "min": "0",
                "max": "100"
            },
            {
                "type": "number",
                "name": "rate_employee_private",
                "label": {
                    "en": "Employee's contribution percentage in the Private Sector",
                    "fr": "Pourcentage de l'employé dans le secteur privé"
                },
                "rights": {
                    "read": "150201",
                    "write": "150202",
                    "update": "150203",
                    "replace": "150206",
                },
                "relevance": "True",
                "default": "0",
                "min": "0",
                "max": "100"
            }
        ],
    },
    {
        "class": "ContractDetails",
        "parameters": [
            {
                "type": "number",
                "name": "income",
                "label": {
                    "en": "Income",
                    "fr": "Salaire"
                },
                "rights": {
                    "read": "152101",
                    "write": "152102",
                    "update": "152103",
                    "replace": "152103",
                },
                "relevance": "True",
                "condition": "INPUT>100",
                "default": ""
            }
        ],
    },
    {
        "class": "PolicyHolderInsuree",
        "parameters": [
            {
                "type": "number",
                "name": "income",
                "label": {
                    "en": "Income",
                    "fr": "Salaire"
                },
                "rights": {
                    "read": "150201",
                    "write": "150202",
                    "update": "150203",
                    "replace": "150206",
                },
                "relevance": "True",
                "condition": "INPUT>100",
                "default": ""
            }
        ],
    },
]

DESCRIPTION_CONTRIBUTION_VALUATION = F"" \
    F"This calcutation will add the income in the contract details " \
    F"and PHinsuree and the percentage in the Contribution plan" \
    F" so when a contract valuation is requested then the calculation will" \
    F" determine the value based on the contract details income and CP percentage"

FROM_TO = []
