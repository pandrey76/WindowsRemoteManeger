#Import apx
Function GetPackageFamilyName([String]$patern, [String]$user)
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

GetPackageFamilyName -patern "alculator" -user "Ogurchuk"
#Write-Host $temp