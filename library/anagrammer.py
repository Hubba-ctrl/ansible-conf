#!/usr/bin/env python3
from ansible.module_utils.basic import AnsibleModule

def reverse(text: str) -> str:
    return text[::-1]

def main() -> None:
    mod = AnsibleModule(
        argument_spec=dict(
            message=dict(type="str", required=False, default="This is a really fun default"),
        ),
        supports_check_mode=True,
    )

    orig_msg = mod.params["message"]
    rev_msg = reverse(orig_msg)

    if orig_msg == "fail me":
        mod.fail_json(
            msg="You requested this to fail",
            changed=True,
            original_message=orig_msg,
            reversed_message=rev_msg
        )
    elif orig_msg == rev_msg:
        mod.exit_json(
            changed=False,
            original_message=orig_msg,
            reversed_message=rev_msg
        )
    else:
        mod.exit_json(
            changed=True,
            original_message=orig_msg,
            reversed_message=rev_msg
        )

if __name__ == "__main__":
    main()
