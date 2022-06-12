def migrate(cr, installed_version):
    cr.execute("""
        UPDATE request_stage_route
        SET button_style = website_button_style;
    """)
