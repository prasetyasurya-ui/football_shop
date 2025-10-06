let toastTimeout;

function showToast(title, message, type = 'normal', duration = 4000) {
    const toastComponent = document.querySelector('#toast-component');
    const toastTitle = document.querySelector('#toast-title');
    const toastMessage = document.querySelector('#toast-message');

    if (!toastComponent) return;

    clearTimeout(toastTimeout);

    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-600');
        toastComponent.style.border = '1px solid #22c55e';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove("opacity-0", "-translate-y-64");
    toastComponent.classList.add("opacity-100", "translate-y-0");

    toastTimeout = setTimeout(() => {
        toastComponent.classList.remove("opacity-100", "translate-y-0");
        toastComponent.classList.add("opacity-0", "-translate-y-64");
    }, duration);

}