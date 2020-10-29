# "./LogoffUser.ps1"

################################################################
# Correcting Work!!!!
<#
function GetPackageFamilyName([String]$patern, [String]$user)
{
    $apx_package = Get-AppxPackage -User $user
    foreach ($apx_pack in $apx_package)
    {
        $temp_str = $apx_pack.PackageFamilyName
        if ($temp_str.Contains($patern))
        {
            Return ($temp_str)
        }
    }
}


function BanCurrentUser([String]$user)
{
    $calculater_id = GetPackageFamilyName -patern "alculator" -user $user
    Set-AssignedAccess -AppUserModelId $calculater_id!app -UserName $user
    # Get-Quser-v2 -user $user
}

BanCurrentUser -user $args[0]
#>
################################################################

function GetPackageFamilyName([String]$AppPattern, [String]$UserName)
{
    $apx_package = Get-AppxPackage -User $UserName
    foreach ($apx_pack in $apx_package)
    {
        $app_full_name = $apx_pack.PackageFamilyName
        if ($app_full_name.ToUpper().Contains($AppPattern.ToUpper()))
        {
            Return ($app_full_name)
        }
    }
}


function BanCurrentUser([String]$UserName, [String]$AppPattern)
{
    $app_family_name = GetPackageFamilyName -AppPattern $AppPattern -user $UserName
    Set-AssignedAccess -AppUserModelId $app_family_name!app -UserName $UserName
}

BanCurrentUser -user $args[0] -AppPattern $args[1]
# C:\Work\WindowsRemoteManeger\PS>powershell "C:\Work\WindowsRemoteManeger\PS\BanUser.ps1" "Ogurchuk" "alculator"
