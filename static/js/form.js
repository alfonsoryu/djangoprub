document.addEventListener('DOMContentLoaded', function() {
    const programSelect = document.getElementById('id_program');
    const subgroupSelect = document.getElementById('id_subgroup');
    const instrumentalFields = document.getElementById('instrumental-fields');
    const coralFields = document.getElementById('coral-fields');
    const ageInput = document.getElementById('id_age');
    const minorFields = document.getElementById('minor-fields');

    function loadSubgroups(programId) {
        if (!programId) return;
        
        fetch(`/ajax/load-subgroups/?program_id=${programId}`)
            .then(response => response.json())
            .then(data => {
                subgroupSelect.innerHTML = '<option value="">---------</option>';
                data.forEach(subgroup => {
                    const option = new Option(subgroup.name, subgroup.id);
                    subgroupSelect.add(option);
                });
            });
    }

    function updateFields() {
        const selectedOption = programSelect.options[programSelect.selectedIndex];
        const isInstrumental = selectedOption.dataset.instrumental === 'true';
        
        instrumentalFields.style.display = isInstrumental ? 'block' : 'none';
        coralFields.style.display = !isInstrumental ? 'block' : 'none';
        
        if (!isInstrumental) {
            loadSubgroups(programSelect.value);
        }
    }

    function updateMinorFields() {
        const age = parseInt(ageInput.value);
        minorFields.style.display = age < 18 ? 'block' : 'none';
    }

    programSelect.addEventListener('change', updateFields);
    ageInput.addEventListener('change', updateMinorFields);
    
    // Initial update
    updateFields();
    updateMinorFields();
});