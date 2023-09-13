import openai
from credential_getter import get_environment_variable
import json

openai.api_key = get_environment_variable("OPENAI_KEY")

class LLMSummarizer():
    def summarize(self, input_text, mode='data_extractor'):
        with open('config.json', 'r') as file:
            self.config = json.load(file)
        if mode == 'data_extractor':
            prompt = self.config['data_extractor']
        elif mode == 'governing_law':
            prompt = self.config['governing_law']
        #: Add the input to the prompt
        prompt += input_text
        # Send the prompt to the model
        response = openai.Completion.create(    
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        # Extract the summary from the response
        summary = response.choices[0].text.strip()
        return summary
    
if __name__ == "__main__":
    from termcolor import colored
    llm_summarizer = LLMSummarizer()

    original = """
COMMERCIAL REAL ESTATE LOAN AGREEMENT
THIS AGREEMENT is made this 1st day of September 2023.
BETWEEN:
ABC BANK, a financial institution duly organized and existing under the laws of the State of New York, having its principal place of business at 123 Main Street, New York, NY 10001 (hereinafter referred to as the "Lender").

XYZ CORPORATION, a corporation duly organized and existing under the laws of the State of California, having its principal place of business at 456 Elm Street, Los Angeles, CA 90001 (hereinafter referred to as the "Borrower").

RECITALS:
WHEREAS, the Borrower has requested the Lender to extend a loan to the Borrower for the purpose of financing the acquisition of a commercial real estate property located at 789 Oak Street, San Francisco, CA 94101;

WHEREAS, the Lender has agreed to extend such a loan to the Borrower on the terms and conditions set forth herein;

NOW, THEREFORE, in consideration of the mutual covenants contained herein and other good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, the parties hereto agree as follows:

ARTICLE 1 – LOAN DETAILS
1.1 Loan Amount

The Lender agrees to lend to the Borrower, and the Borrower agrees to borrow from the Lender, the principal amount of TEN MILLION UNITED STATES DOLLARS (US$10,000,000) (the "Loan").

1.2 Interest Rate

The Loan shall bear interest at a rate of three and a half percent (3.5%) per annum, calculated on the basis of a 360-day year for the actual number of days elapsed.

1.3 Loan Term

The term of the Loan shall be ten (10) years, commencing on the date hereof and ending on the 1st day of September 2033, unless sooner terminated in accordance with the terms hereof.

1.4 Repayment

The Borrower shall repay the Loan in quarterly installments of principal and interest, with the first installment due on December 1, 2023, and subsequent installments due on the first day of each quarter thereafter.

ARTICLE 2 – REPRESENTATIONS AND WARRANTIES
The Borrower hereby represents and warrants to the Lender as follows:

2.1 Organization and Good Standing

The Borrower is a corporation duly organized, validly existing, and in good standing under the laws of the State of California.

2.2 Authority

The Borrower has full corporate power and authority to enter into this Agreement and to perform its obligations hereunder.

(Additional representations and warranties would include details regarding no conflicts, litigation, accuracy of information, etc.)

ARTICLE 3 – COVENANTS
The Borrower covenants and agrees with the Lender as follows:

3.1 Affirmative Covenants

The Borrower shall:

(a) maintain its corporate existence and good standing;
(b) comply with all laws applicable to its business and operations;
(c) maintain insurance on the property securing the Loan in such amounts and against such risks as is customary for similar properties in the locality;

(Additional affirmative and negative covenants would be detailed in this section, including financial reporting requirements, restrictions on indebtedness, etc.)

ARTICLE 4 – EVENTS OF DEFAULT
The following shall constitute events of default under this Agreement:

4.1 Non-Payment

Failure by the Borrower to pay any amount due under this Agreement within ten (10) days of the due date.

4.2 Breach of Representation

Any representation or warranty made by the Borrower herein proves to have been incorrect in any material respect when made.

(Additional events of default would be detailed in this section, including bankruptcy events, cross-defaults to other agreements, etc.)

ARTICLE 5 – MISCELLANEOUS
5.1 Notices

Any notice or other communication required or permitted to be given hereunder shall be in writing and shall be deemed to have been duly given when delivered in person, or sent by registered mail, to the respective parties at the addresses set forth above.

5.2 Governing Law

This Agreement shall be governed by and construed in accordance with the laws of the State of New York, without regard to conflict of laws principles.

(Additional miscellaneous provisions would include details regarding amendments, waivers, severability, etc.)

IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first above written.
ABC BANK
By:_________________
Name: John Doe
Title: Vice President

XYZ CORPORATION
By:_________________
Name: Jane Smith
Title: Chief Executive Officer

DISCLAIMER: THIS DOCUMENT IS A FICTIONAL REPRESENTATION CREATED FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY. IT IS NOT INTENDED TO BE USED FOR ANY REAL LEGAL OR COMMERCIAL TRANSACTIONS.

    """

    summary = llm_summarizer.summarize(original, mode='data_extractor')

    print(colored(f"original: {original}", 'blue'))
    print(colored(f"summary: {summary}", 'yellow'))
