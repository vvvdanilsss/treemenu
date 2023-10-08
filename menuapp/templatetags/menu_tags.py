from django import template
from django.urls import resolve
from menuapp.models import MenuItem
from django.db.models import Prefetch

register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    current_view = resolve(current_url).url_name
    active_items = []
    expand_items = []  # Элементы для раскрытия

    all_menu_items = MenuItem.objects.filter(menu_name=menu_name)

    for item in all_menu_items:
        if item.named_url and item.named_url == current_view:
            active_items.append(item.name)

            # Добавляем родительские элементы
            parent = item.parent
            while parent:
                expand_items.append(parent.name)
                parent = parent.parent

            # Добавляем первый уровень дочерних элементов
            for child in item.children.all():
                expand_items.append(child.name)

    root_items = MenuItem.objects.filter(menu_name=menu_name, parent=None).prefetch_related(
        Prefetch('children', queryset=MenuItem.objects.all())
    )
    return {'items': root_items, 'active_items': active_items, 'expand_items': expand_items}
