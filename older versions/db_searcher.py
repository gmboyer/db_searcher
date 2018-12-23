### DB searcher ###
# An interactive GUI for selecting, filtering,
# sorting, joining, and exporting csv data.
# Author: Grayson Boyer

# This code was designed to work in a Python 3 Jupyter notebook
# with the following code in the first cell:

# from db_searcher import *
# main()


# import packages
from ipywidgets import interact, interactive, fixed, interact_manual, HBox, VBox, Output
import ipywidgets as widgets
from IPython.display import display, clear_output
from dfply import *
import pandas as pd
import sys


def main():


    # define starting widgets
    import_csv_form = widgets.Text(value = '', placeholder = 'name of csv to import', description = 'csv:', disabled = False)
    condition_dropdown = widgets.Dropdown(options = ['Select', 'Sort', 'Filter', 'Join', 'Export'], value = 'Select', description = 'condition:', disabled = False)
    add_button = widgets.Button(description = "Add")
    remove_button = widgets.Button(description = "Remove")
    search_button = widgets.Button(description = "Search")

    # define vbox of starting widgets
    add_search_vbox = widgets.VBox([widgets.HBox([condition_dropdown, add_button, remove_button]), widgets.HBox([import_csv_form, search_button])])

    # display vbox of starting widgets
    display(add_search_vbox)

    # empty lists that will contain widget rows
    row_widget_contents = [] # stores row widgets
    row_type_contents = [] # stores row type as string (e.g. "Select", "Sort", "Filter"...)

    # functions for creating select, sort, filter, join, and export rows
    def create_select_row():
        return widgets.Text(value = '', placeholder = 'Column(s) to select', description = 'Select:', disabled = False)

    def create_sort_row():
        return widgets.Text(value = '', placeholder = 'Column(s) to sort by', description = 'Sort by:', disabled = False)

    def create_filter_row():
        return widgets.HBox([widgets.Text(value = '', placeholder = 'Column', description = 'Filter:', disabled = False), widgets.Text(value = '', placeholder = 'e.g. > 50', description = 'Criteria:', disabled = False)])

    def create_join_row():
        return widgets.HBox([
            widgets.Text(value = '', placeholder = 'name of csv to join', description = 'csv:', disabled = False),
            widgets.Dropdown(options = ['inner', 'outer', 'left', 'right', 'anti'], value = 'inner', description = 'Join type:', disabled = False),
            widgets.Text(value = '', placeholder = 'column used to join', description = 'column:', disabled = False)])

    def create_export_row():
        return widgets.Text(value = '', placeholder = 'name of exported csv', description = 'Export as:', disabled = False)

    # function that runs when the 'add row' button is clicked
    def on_add_button_clicked(b):
        if condition_dropdown.value == 'Select':
            row_widget_contents.append(create_select_row())
            row_type_contents.append('Select')

        if condition_dropdown.value == 'Sort':
            row_widget_contents.append(create_sort_row())
            row_type_contents.append('Sort')

        if condition_dropdown.value == 'Filter':
            row_widget_contents.append(create_filter_row())
            row_type_contents.append('Filter')

        if condition_dropdown.value == 'Join':
            row_widget_contents.append(create_join_row())
            row_type_contents.append('Join')

        if condition_dropdown.value == 'Export':
            row_widget_contents.append(create_export_row())
            row_type_contents.append('Export')

        clear_output(True)
        display(widgets.VBox(row_widget_contents + [add_search_vbox]))

    # function that runs when the 'remove row' button is clicked
    def on_remove_button_clicked(b):
        if len(row_widget_contents) > 0:
            row_widget_contents.pop(-1)
            row_type_contents.pop(-1)
            clear_output(True)
            display(widgets.VBox(row_widget_contents + [add_search_vbox]))

    # function that runs when the 'search' button is clicked
    def on_search_button_clicked(b):
        # clear previous output
        clear_output(True)
        # reset flag for exporting
        flag_export = False

        # load the csv that will be searched as the variable 'data'
        try:
            data = pd.read_csv(import_csv_form.value + '.csv')
        except:
            display(widgets.VBox(row_widget_contents + [add_search_vbox]))
            print("Please specify a valid csv.")
            return

        # display widgets
        display(widgets.VBox(row_widget_contents + [add_search_vbox]))

        # begin modifying the action that will be evaluated at the end
        action = "data" # action starts with loaded csv contents 'data'
        for i in range(len(row_type_contents)):
            if row_type_contents[i] == 'Select':
                selected_columns = ["X." + x.strip() for x in row_widget_contents[i].value.split(',')]
                action = action + " >>  select(%s)" % ", ".join(selected_columns)

            if row_type_contents[i] == 'Sort':
                selected_columns = ["X." + x.strip() for x in row_widget_contents[i].value.split(',')]
                action = action + " >>  arrange(%s)" % ", ".join(selected_columns)

            if row_type_contents[i] == 'Filter':
                action = action + " >>  mask(X.%s %s)" % (row_widget_contents[i].children[0].value, row_widget_contents[i].children[1].value)

            if row_type_contents[i] == 'Join':
                csv_to_join = pd.read_csv(row_widget_contents[i].children[0].value + '.csv')
                join_type = row_widget_contents[i].children[1].value
                join_column = row_widget_contents[i].children[2].value
                action = action + " >> " + join_type + "_join(csv_to_join, by = '" + join_column + "')"

            if row_type_contents[i] == 'Export':
                flag_export = True
                export_filename = row_widget_contents[i].value

        # print current 'search' action
        print(action)

        # evaluate current action and display result
        display(eval(action))

        # if search result is flagged for export, export dataframe as a csv
        if flag_export == True:
            try:
                eval(action).to_csv(export_filename + '.csv', sep=',', encoding = 'utf-8')
            except:
                clear_output(True)
                display(widgets.VBox(row_widget_contents + [add_search_vbox]))
                print("Could not export csv. If the csv is open, try closing it.")
                return

    # specify which functions to run with buttons
    add_button.on_click(on_add_button_clicked)
    remove_button.on_click(on_remove_button_clicked)
    search_button.on_click(on_search_button_clicked)


if __name__ == '__main__':
    main()
