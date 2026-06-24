class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        to_send = set()
        for email in emails:
            local, domain = email.split('@')
            normalized_local = local.replace(".","").split("+")[0]
            to_send.add(tuple([normalized_local, domain]))
        return len(to_send)