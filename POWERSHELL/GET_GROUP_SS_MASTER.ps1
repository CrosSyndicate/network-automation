$adgroups = "group1", "group2"
# changed group names to generic names for at home work

#$filter = (EmailAddress -notlike '*@tpg.com') - passing this variable into function broke it, no output
#The above comment was solved using a custom object with @{name = "groupname";expression ={$group}}


$results = @();

foreach ($group in $adgroups) 

{
   $results+= (Get-ADGroupMember -Identity $group -Recursive | Get-ADUser -Properties DisplayName | Select-Object name, SamAccountName, DisplayName, @{name = "groupname";expression ={$group}})

}

$results | Export-CSV -Path “group_output.csv”

# -Filter {(EmailAddress -notlike '*@tpg.com')} - Trying to use this to filter only non @tpg.com emails - it's pulling every non TPG email