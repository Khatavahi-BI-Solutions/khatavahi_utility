from . import __version__ as app_version

app_name = "khatavahi_utility"
app_title = "Khatavahi Utility"
app_publisher = "Jigar Tarpara"
app_description = "Utility that can use with frappe"
app_email = "jigartarpara@khatavahi.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/khatavahi_utility/css/khatavahi_utility.css"
# app_include_js = "/assets/khatavahi_utility/js/khatavahi_utility.js"

# include js, css files in header of web template
# web_include_css = "/assets/khatavahi_utility/css/khatavahi_utility.css"
# web_include_js = "/assets/khatavahi_utility/js/khatavahi_utility.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "khatavahi_utility/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "khatavahi_utility.utils.jinja_methods",
#	"filters": "khatavahi_utility.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "khatavahi_utility.install.before_install"
# after_install = "khatavahi_utility.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "khatavahi_utility.uninstall.before_uninstall"
# after_uninstall = "khatavahi_utility.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "khatavahi_utility.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"khatavahi_utility.tasks.all"
#	],
#	"daily": [
#		"khatavahi_utility.tasks.daily"
#	],
#	"hourly": [
#		"khatavahi_utility.tasks.hourly"
#	],
#	"weekly": [
#		"khatavahi_utility.tasks.weekly"
#	],
#	"monthly": [
#		"khatavahi_utility.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "khatavahi_utility.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "khatavahi_utility.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "khatavahi_utility.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"khatavahi_utility.auth.validate"
# ]
