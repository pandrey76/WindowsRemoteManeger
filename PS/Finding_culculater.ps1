
Function GetPackageFamilyName([String]$patern, [String]$user)
{

    $apx_package = Get-AppxPackage -User $user
    foreach ($apx_pack in $apx_package)
    {
        $temp_str = $apx_pack.PackageFamilyName
        if ($temp_str.Contains(patern))#alculator
        {
            Return ($temp_str)
        }
    }
}

GetPackageFamilyName(alculator, "Ogurchuk")
