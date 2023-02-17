#script has been edited to use generic username and domain names

| Get-ADUSER -Properties Name, Mail 


ad_group_1_redacted, ad_group_2_redacted

C:\Users\%USERNAME%

Get-ADGroupMember -Identity ad_group_1_redacted | Select-Object name, objectClass,distinguishedName | Export-CSV -Path “adgroupmembers.csv”





$adgroups = "ad_group_1_redacted", "ad_group_2_redacted"

$results = @();

foreach ($group in $adgroups) 

{
   $results+= (Get-ADGroupMember -Identity $group -Recursive)

}

$results | Format-Table -AutoSize | Export-CSV -Path “adgroupmembers.csv”



Get-ADGroupMember -Identity "ad_group_1_redacted" | Get-ADUser -Filter * -Properties EmailAddress,DisplayName, samaccountname| Select name, SamAccountName, EmailAddress, DisplayName | Export-Csv "test_single.csv"