document.addEventListener('DOMContentLoaded', function(){
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const customConfirmBox = document.getElementById('customConfirmBox');
    const confirmDeleteBtn = document.querySelector('.confirm-delete');
    const confirmCancelBtn = document.querySelector('.confirm-cancel');

    let deleteForm = null;

    deleteButtons.forEach(button =>{
        button.addEventListener('click', function(e){
            e.preventDefault();
            deleteForm = this.closest('form');
            customConfirmBox.style.display = 'flex';
        });
    });

    confirmDeleteBtn.addEventListener('click', function(){
        if(deleteForm){
            deleteForm.submit();
        }
        customConfirmBox.style.display = 'none';
    });

    confirmCancelBtn.addEventListener('click', function(){
        customConfirmBox.style.display = 'none';
    });
})