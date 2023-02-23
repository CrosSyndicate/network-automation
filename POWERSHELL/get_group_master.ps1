$adgroups = "group1", "group2"
# changed group names to generic names for at home work

#$filter = (EmailAddress -notlike '*@DOMAIN.com') - passing this variable into function broke it, no output
#The above comment was solved using a custom object with @{name = "groupname";expression ={$group}}


$results = @();

foreach ($group in $adgroups) 

{
   $results+= (Get-ADGroupMember -Identity $group -Recursive | Get-ADUser -Properties DisplayName | Select-Object name, SamAccountName, DisplayName, @{name = "groupname";expression ={$group}})
}

$results | Export-CSV -Path “group_output.csv” -NoTypeInformation -Force

#added to the $results CSV export, -NoTypeInformation to remove header in CSV - just making it cleaner to read

# -Filter {(EmailAddress -notlike '*@DOMAIN.com')} - Trying to use this to filter only non @DOMAIN.com emails - it's pulling every non DOMAIN email