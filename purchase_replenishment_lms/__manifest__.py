# Copyright (C) 2026 Vertel Sverige AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Replenishment: Training (LMS)',
    'version': '18.0.1.0.0',
    'summary': 'eLearning course on purchase proposals and reordering rules',
    'category': 'Purchase/Training',
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se',
    'license': 'AGPL-3',
    'maintainer': 'Vertel Sverige AB',
    'description': """
Purchase Replenishment LMS
==========================
Training material delivered as a website_slides course.

Explains how Odoo 18 builds purchase proposals (RFQs) from reordering
rules (stock.warehouse.orderpoint):

- Section 1: The reordering rule (Min / Max / Multiple)
- Section 2: How the replenishment proposal is calculated
- Section 3: Order Deadline vs Expected Arrival
- Section 4: Troubleshooting — why a proposal looks wrong

Includes Mermaid-generated diagrams and Odoo page builder articles.
    """,
    'depends': [
        'website_slides',
    ],
    'data': [
        'data/slide_channel.xml',
        'data/slide_slides_s1.xml',
        'data/slide_slides_s2.xml',
        'data/slide_slides_s3.xml',
        'data/slide_slides_s4.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
