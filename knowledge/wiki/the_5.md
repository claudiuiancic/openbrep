---
id: wiki.generated.the
type: wiki
category: other
commands: ["THE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### THE BACKWARD MIGRATION SCRIPT

Via the Backward Migration script you can define the backward conversion logic converting new object instances to older ones. For more and detailed information, please take a look at the section called “Backward Migration script”.

targetGUID = TO_GUID ! ============================================================================== ! Subroutines ! ============================================================================== gosub "migrationstepname_BWM" ! ============================================================================== ! Set Migration GUID ! ============================================================================== setmigrationguid targetGUID

! ============================================================================== end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! en ! ==============================================================================

! ============================================================================== ! migrationstepname ! ============================================================================== "migrationstepname _BWM":

if targetGUID # "" then bMigrationSuccess = 1 if bMigrationSuccess = 1 then

oldParameter = newParameter parameters oldParameter = oldParameter

else

targetGuid = "" endif

endif return

TO_GUID is the global variable holding the main ID of the target element in the conversion. Use the SETMIGRATIONGUID command for setting targetGUID.