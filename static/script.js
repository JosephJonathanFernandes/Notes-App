document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.notes-container');
  if (container) {
    container.addEventListener('click', async (event) => {
      const deleteButton = event.target.closest('.delete-button');
      if (deleteButton) {
        const itemId = deleteButton.dataset.noteId;
        const response = await fetch(`/del/${itemId}`, {
          method: 'POST',
        });
        if (response.ok) {
          window.location.reload();
        } else {
          console.error('Failed to delete note');
        }
      }
    });
  } else {
    console.error('Notes container element not found');
  }
});