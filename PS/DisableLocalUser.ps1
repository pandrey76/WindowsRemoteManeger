function Disable-CurrentUser([String]$user)
{
    Disable-LocalUser -Name $user
}

Disable-CurrentUser -user $args[0]