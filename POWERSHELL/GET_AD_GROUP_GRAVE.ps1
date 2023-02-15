$adgroups = "app_okta_investran_ssp_prod", "app_okta_investran_uat_ssp"
$filter = (EmailAddress -notlike '*@tpg.com')


$results = @();

foreach ($group in $adgroups) 

{
   $results+= (Get-ADGroupMember -Identity $group -Recursive | Get-ADUser -Properties EmailAddress -Filter $filter | Select name, SamAccountName, EmailAddress)

}

$results | Export-CSV -Path “newtest2.csv”

# -Filter {(EmailAddress -notlike '*@tpg.com')} - Trying to use this to filter only non @tpg.com emails - it's pulling every non TPG email