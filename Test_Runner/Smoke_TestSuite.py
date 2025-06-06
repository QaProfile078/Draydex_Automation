import argparse
import subprocess

def smoke_test_suite(email_id,password,server):
    subprocess.run([
        'behave',
        '--stop',
        'features/TC03_CreateQuote.feature',
        'features/TC03_CheckCreatedQuoteOnDashboardPage.feature',
        'features/TC03_CheckCreatedQuoteOnRateQuotesPage.feature',
        'features/TC06_Update_Quote.feature',
        'features/TC04_Send_To_Carrier.feature',
        'features/TC05_Add_Rate.feature',
        'features/TC09_Delete_Rate.feature',
        'features/TC05_Add_Rate.feature',
        'features/TC08_Select_spot.feature',
        'features/TC07_Delete_Quote.feature',
        # '--no-capture',
        '--define', f'EMAIL_ID={email_id}',
        '--define', f'PASSWORD={password}',
        '--define', f'SERVER={server}'
    ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email_id', required=True, help='Email ID to pass into Behave tests for login')
    parser.add_argument('--password', required=True, help='Password to pass into Behave tests for login')
    parser.add_argument('--server', required=True, help='Login server on which Behave tests should run')
    args = parser.parse_args()

    smoke_test_suite(args.email_id, args.password,args.server)
