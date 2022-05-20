import re

class Cleaning:
    def __init__(self):
        return

# Fill Corrigo Status from Column Customer Name Extract Status 
# ==================================================================
    def corrigo_status(self, df):
        status = re.findall("\((.*?)\)", df["Customer Name"])
        if len(status) > 0 and len(status) < 2:
            return str(status[0])
        elif len(status) > 1:
            join_status = " | ".join(status)
            return join_status
        else:
            return None


# Fill Site comment from Column Customer Name Extract Site comment 
# ==================================================================
    def site_comment(self, df):
        comment = re.findall("\[(.*?)\]", df["Customer Name"])
        if len(comment) > 0 and len(comment) < 2:
            return str(comment[0])
        elif len(comment) > 1:
            join_comment = " | ".join(comment)
            return join_comment
        else:
            return None

# History Status T/F Convert Bit 1 or 0 for Column Historical Status?
# ==================================================================
    def bitify(self, df):
        if df['Historical Status?'] == "Yes":
            return True
        else:
            return False
