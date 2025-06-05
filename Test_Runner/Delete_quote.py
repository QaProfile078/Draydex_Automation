import argparse
import subprocess

def Delete_Existing_Quote(email_id,password,quote_id,server):
    subprocess.run([
        'behave',
        'features/TC07_Delete_Quote.feature',
        'features/TC07_CheckDeletedQuoteOnDashboardPage.feature',
        'features/TC07_CheckDeletedQuoteOnRateQuotesPage.feature',
        '--no-capture',
        '--define', f'EMAIL_ID={email_id}',
        '--define', f'PASSWORD={password}',
        '--define', f'SERVER={server}',
        '--define', f'QUOTE_ID={quote_id}'
    ])

def Create_and_Delete_New_Quote(email_id,password,server):
    subprocess.run([
        'behave',
        'features/TC03_CreateQuote.feature',
        'features/TC03_CheckCreatedQuoteOnDashboardPage.feature',
        'features/TC03_CheckCreatedQuoteOnRateQuotesPage.feature',
        'features/TC07_Delete_Quote.feature',
        'features/TC07_CheckDeletedQuoteOnDashboardPage.feature',
        'features/TC07_CheckDeletedQuoteOnRateQuotesPage.feature',
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
    parser.add_argument('--quote_id', required=False, help='Quote_id to pass into Behave tests for deletion')
    args = parser.parse_args()

    if args.quote_id:
        Delete_Existing_Quote(args.email_id, args.password, args.quote_id,args.server)
    else:
        Create_and_Delete_New_Quote(args.email_id, args.password,args.server)

