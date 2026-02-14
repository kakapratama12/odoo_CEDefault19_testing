# script to debug registry
import sys

# Flush any pending output
sys.stdout.flush()

try:
    registry = env.registry
    print(f"Total models in registry: {len(registry)}")

    m1 = 'account_financial_report_abstract_wizard'
    if m1 in registry:
        print(f"Model {m1}: FOUND")
    else:
        print(f"Model {m1}: MISSING")

    m2 = 'trial.balance.report.wizard'
    if m2 in registry:
        print(f"Model {m2}: FOUND")
    else:
        print(f"Model {m2}: MISSING")

    print("\nAttempting manual import...")
    import odoo.addons.account_financial_report.wizard.trial_balance_wizard as tbw
    print("Import SUCCESS:", tbw)
    
    # Check if we can instantiate it manually (just class check)
    cls = tbw.TrialBalanceReportWizard
    print("Class definition found:", cls)
    print("Class _name:", cls._name)

except Exception as e:
    print("\nEXCEPTION CAUGHT during debug script:")
    print(e)
    import traceback
    traceback.print_exc()
