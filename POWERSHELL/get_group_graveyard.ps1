$adgroups = "group1", "group2"
$filter = (EmailAddress -notlike '*@domain.com')
#deleted work specific groups and domains from this script

$results = @();

foreach ($group in $adgroups) 

{
   $results+= (Get-ADGroupMember -Identity $group -Recursive | Get-ADUser -Properties EmailAddress -Filter $filter | Select name, SamAccountName, EmailAddress)

}

$results | Export-CSV -Path “newtest2.csv”

# -Filter {(EmailAddress -notlike '*@domain.com')} - Trying to use this to filter only non @domain.com emails - it's pulling every non DOMAIN email