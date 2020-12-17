function Enable-CurrentUser([String]$user)
{
    # New-Item -ItemType File -Path "c:/temp.err" -Force
    # Out-File -FilePath "c:/temp.err" -InputObject $user

    Enable-LocalUser -Name $user

}

Enable-CurrentUser -user $args[0]