Get-ADGroupMember -Identity "app_okta_investran_ssp_prod" -Recursive | 
Get-ADUser -Properties EmailAddress | 
Select name, SamAccountName, EmailAddress, DisplayName | 
Export-Csv "test_single2.csv"