from flask import url_for


def get_experts(expert=None):
    """Generate the expert definitions. This needs to be done in a function so
    that it can be called when the app context is available. This is so
    that the url_for() methods work.
    :param expert: A optional expert. If provided this method will only
        return that expert.
    :returns: One or all experts.
    """
    experts = {
        "omnivector": {
            "name": "Omnivector",
            "username": "omnivector",
            "page_url": url_for("jaasai.experts_omnivector"),
            "logo": (
                "https://assets.ubuntu.com/v1/"
                "9681b99c-OV+Logo+Horiz+3color.svg"
            ),
            "logo_invert": (
                "https://assets.ubuntu.com/v1/"
                "9681b99c-OV+Logo+Horiz+3color.svg"
            ),
            "highlights": [
                "Workflow solutions that enable enterprise processing"
                + " at scale",
                "Distributed processing and storage platform architecture",
                "DevOPS/DataOPS design and implementation",
                "Data processing and batch enrichment",
            ],
            "website": "https://www.omnivector.solutions",
            "email": "info@omnivector.solutions",
            "phone_numbers": [
                {
                    "number": "+14134897005",
                    "display": "+1 (413) 489 7005",
                    "location": "USA",
                }
            ],
            "store_card": {
                "heading": ("Smart, Flexible, Scalable. No strings attached."),
                "button_label": "Big data experts",
            },
        },
        "spiculecharms": {
            "name": "Spicule",
            "username": "spiculecharms",
            "page_url": url_for("jaasai.experts_spicule"),
            "logo": (
                "https://assets.ubuntu.com/v1/"
                "c7881d6c-spiculelogo-spacingx2-01.svg"
            ),
            "logo_invert": (
                "https://assets.ubuntu.com/v1/"
                "cdad8056-spiculelogo-white.svg"
            ),
            "highlights": [
                "Spicule&rsquo;s solutions can solve your Big Data challenges",
                "Supported analytics",
                "Streaming data platforms",
            ],
            "website": "http://www.spicule.co.uk",
            "email": "info@spicule.co.uk",
            "phone_numbers": [
                {
                    "number": "+441603327762",
                    "display": "+44 (0) 1603 327762",
                    "location": "UK",
                },
                {
                    "number": "+18448141689",
                    "display": "+1 (0) 8448 141689",
                    "location": "USA",
                },
            ],
            "store_card": {
                "heading": (
                    "Spicule&rsquo;s solutions can solve your Big Data "
                    "challenge."
                ),
                "button_label": "Big data experts",
            },
        },
    }
    if expert:
        return experts.get(expert)
    else:
        return experts
