import argparse
import subprocess


def Add_Rate_to_new_quote(email_id,password,server):
    subprocess.run([
        'behave',
        'features/TC03_CreateQuote.feature',
        'features/TC05_Add_Rate.feature',
        '--no-capture',
        '--define', f'EMAIL_ID={email_id}',
        '--define', f'PASSWORD={password}',
        '--define', f'SERVER={server}',
    ])

def Add_Rate_to_existing_quote(email_id,password,quote_id,server):
    subprocess.run([
        'behave',
        'features/TC05_Add_Rate.feature',
        '--no-capture',
        '--define', f'EMAIL_ID={email_id}',
        '--define', f'PASSWORD={password}',
        '--define', f'SERVER={server}',
        '--define', f'QUOTE_ID={quote_id}',
    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email_id', required=True, help='Email ID to pass into Behave tests for login')
    parser.add_argument('--password', required=True, help='Password to pass into Behave tests for login')
    parser.add_argument('--server', required=True, help='Login server on which Behave tests should run')
    parser.add_argument('--quote_id', required=False, help='Quote_id to pass into Behave tests for deletion')
    args = parser.parse_args()

    if args.quote_id:
        Add_Rate_to_existing_quote(args.email_id,args.password,args.quote_id,args.server)
    else:
        Add_Rate_to_new_quote(args.email_id, args.password,args.server)