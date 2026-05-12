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

#### THE FORWARD MIGRATION SCRIPT

If an element is changed completely in a newer library, compatibility can be maintained by defining the migration logic. For more detailed information, please take a look at the section called “Forward Migration script”.

actualGUID = FROM_GUID ! ============================================================================== ! Subroutines ! ==============================================================================

_startID = "AAAA-AAAA-...AAA" _endID = "BBBB-BBBB-...BBB"

gosub "migrationstepname_FWM" ! ============================================================================== ! Set Migration GUID ! ============================================================================== setmigrationguid actualGUID

! ============================================================================== end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! end ! en ! ==============================================================================

! ============================================================================== ! migrationstepname ! ============================================================================== "migrationstepname_FWM":

if actualGuid = _startID then newParameter = oldParameter parameters newParameter = newParameter actualGuid = _endID

endif return

FROM_GUID is the global variable holding the main ID of the original object which the migration is run on. In case the script succeeds, the instance gets substituted by the new element with the updated parameters.