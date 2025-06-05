import argparse
import subprocess

def Carrier_details_page(email_id,password,server):
    subprocess.run([
        'behave',
        'features/TC03_CreateQuote.feature',
        'features/TC03_CheckCreatedQuoteOnDashboardPage.feature',
        'features/TC03_CheckCreatedQuoteOnRateQuotesPage.feature',
        '--no-capture',
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

    Carrier_details_page(args.email_id, args.password,args.server)
