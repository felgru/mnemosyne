#
# criterion_wdgt_default.py <Peter.Bienstman@UGent.be>
#

from PyQt4 import QtCore, QtGui

from mnemosyne.libmnemosyne.translator import _
from mnemosyne.libmnemosyne.ui_components.criterion_widget \
     import CriterionWidget
from mnemosyne.libmnemosyne.criteria.default_criterion import DefaultCriterion
from mnemosyne.pyqt_ui.tag_tree_wdgt import TagsTreeWdgt
from mnemosyne.pyqt_ui.card_type_tree_wdgt import CardTypesTreeWdgt
from mnemosyne.pyqt_ui.ui_criterion_wdgt_default import Ui_DefaultCriterionWdgt


class DefaultCriterionWdgt(QtGui.QWidget, Ui_DefaultCriterionWdgt,
                           CriterionWidget):

    """Note that this dialog can support active tags and forbidden tags,
    but not at the same time, in order to keep the interface compact.

    """

    used_for = DefaultCriterion

    def __init__(self, component_manager, parent):
        CriterionWidget.__init__(self, component_manager)
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.card_type_tree_wdgt = CardTypesTreeWdgt(component_manager, self)
        # Bug in Qt: need to explicitly reset the text of this label.
        self.label.setText(_("Activate cards from these card types:"))
        self.gridLayout.addWidget(self.card_type_tree_wdgt, 1, 0)
        self.tag_tree_wdgt = TagsTreeWdgt(component_manager, self)
        self.gridLayout.addWidget(self.tag_tree_wdgt, 1, 1)
        self.parent_saved_sets = parent.saved_sets
        criterion = DefaultCriterion(self.component_manager)
        for tag in self.database().tags():
            criterion._tag_ids_active.add(tag._id)
        self.display_criterion(criterion)
        self.card_type_tree_wdgt.tree_wdgt.\
            itemChanged.connect(self.criterion_changed)
        self.tag_tree_wdgt.tree_wdgt.\
            itemChanged.connect(self.criterion_changed)

    def display_criterion(self, criterion):
        self.card_type_tree_wdgt.display(criterion)
        self.tag_tree_wdgt.display(criterion)
        if len(criterion._tag_ids_forbidden):
            self.active_or_forbidden.setCurrentIndex(1)
        else:
            self.active_or_forbidden.setCurrentIndex(0)

    def criterion(self):

        """Build the criterion from the information the user entered in the
        widget.

        """

        criterion = DefaultCriterion(self.component_manager)
        criterion = self.card_type_tree_wdgt.checked_to_criterion(criterion)
        # Tag tree contains active tags.
        if self.active_or_forbidden.currentIndex() == 0:
            self.tag_tree_wdgt.checked_to_active_tags_in_criterion(criterion)
        # Tag tree contains forbidden tags.
        else:
            self.tag_tree_wdgt.\
                checked_to_forbidden_tags_in_criterion(criterion)
            for tag in self.database().tags():
                criterion._tag_ids_active.add(tag._id)
        return criterion

    def criterion_changed(self):
        self.parent_saved_sets.clearSelection()

    def closeEvent(self, event):
        # This allows the state of the tag tree to be saved.
        self.tag_tree_wdgt.close()