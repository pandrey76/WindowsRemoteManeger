LogoffUser.ps1
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
    Get-Quser-v2 -user $user
}

BanCurrentUser -user "Ogurchuk"