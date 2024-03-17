import { EyeOffIcon, ListPlus, FileTextIcon, FileTypeIcon, SigmaIcon } from "lucide-react"

export const statuses = [
  {
    value: "inconsistent",
    label: "Inconsistent",
    style: "warning",
    action: "Embed",
    actionMessage: "This document is incorrectly embedded. This action will re-embed the document. Are you sure?",
    groupActionMessage: "The selected documents are incorrectly embedded. This action will re-embed them. Documents that are already embedded correctly won't be affected. Are you sure?",
    actionIcon: SigmaIcon
  },
  {
    value: "concealed",
    label: "Concealed",
    style: "disabled",
    action: "Enable",
    actionMessage: "This action will enable this document. The chatbot will be able to answer question about it. Are you sure?",
    groupActionMessage: "This action will enable the selected documents. Documents that are already enabled correctly won't be affected. Are you sure?",
    actionIcon: ListPlus
  },
  {
    value: "enabled",
    label: "Enabled",
    style: "successful",
    action: "Conceal",
    actionMessage: "This action will conceal this document. The chatbot won't be able to answer question about it. Are you sure?",
    groupActionMessage: "This action will conceal the selected documents. Documents that are already concealed correctly won't be affected. Are you sure?",
    actionIcon: EyeOffIcon
  },
  {
    value: "not embedded",
    label: "Not Embedded",
    style: "error",
    action: "Embed",
    actionMessage: "This action will embed this document. Are you sure?",
    groupActionMessage: "This action will embed the selected documents. Documents that are already embedded correctly won't be affected. Are you sure?",
    actionIcon: SigmaIcon
  },
]

export const types = [
  {
    value: "pdf",
    label: "PDF",
    action: "View content",
    icon: FileTextIcon,
  },
  {
    value: "docx",
    label: "DOCX",
    action: "Download",
    icon: FileTypeIcon,
  },
]
