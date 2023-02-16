Get-ADGroupMember -Identity "group1" -Recursive | 
Get-ADUser -Properties EmailAddress | 
Select name, SamAccountName, EmailAddress, DisplayName | 
Export-Csv "test_single2.csv"

#note it's probably better to use DisplayName object rather than Email address because it contains the information I was looking for
#modified group name to maintain security