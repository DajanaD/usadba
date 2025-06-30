$(document).ready(function() {
    $('.jsAddToCart').on('click', function(e) {
        e.preventDefault();
        const productId = $(this).data('product-id');
        const variantId = $(this).data('variant-id');
        const quantity = $(this).closest('form').find('input[name="amount"]').val() || 1;

        $.ajax({
            url: '/ajax/add_to_cart.php',
            type: 'POST',
            data: {
                product_id: productId,
                variant_id: variantId,
                quantity: quantity
            },
            success: function(response) {
                $('#cart_inform').fadeIn().delay(3000).fadeOut();
                updateCartCounter(response.total_items);
            }
        });
    });
});