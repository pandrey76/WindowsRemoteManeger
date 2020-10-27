# "./LogoffUser.ps1"


function GetPackageFamilyName([String]$patern, [String]$user)
{
    $apx_package = Get-AppxPackage -User $user # | Out-File -FilePath "c:\\apx_package.txt"
#    Write-Host $apx_package

    foreach ($apx_pack in $apx_package)
    {
        $temp_str = $apx_pack.PackageFamilyName
        if ($temp_str.Contains($patern))
        {
            Write-Host $temp_str
            Return ($temp_str)
        }
    }
}


function BanCurrentUser([String]$user)
{
    Write-Host  $user
    $calculater_id = GetPackageFamilyName -patern "alculator" -user $user
    Set-AssignedAccess -AppUserModelId $calculater_id!app -UserName $user
    # Get-Quser-v2 -user $user
}

 BanCurrentUser -user $args[0]