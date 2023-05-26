from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        actual_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            actual_email = local + '@' + domain
            actual_emails.add(actual_email)

        return len(actual_emails)