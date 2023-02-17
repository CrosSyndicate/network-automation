$adgroups = "group1", "group2"
$results = @();

foreach ($group in $adgroups) 
{
   $results+= (Get-ADGroupMember -Identity $group -Recursive | Get-ADUser -Properties DisplayName | Select-Object DisplayName, @{name = "groupname";expression ={$group}})

}

$results | Export-CSV -Path “group_users.csv” -NoTypeInformation -Force
