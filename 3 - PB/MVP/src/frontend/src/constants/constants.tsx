import { NavItems } from '@/types/types';
import {
  BotMessageSquareIcon,
  FolderOpenIcon,
  GalleryVerticalEndIcon,
  SettingsIcon,
  EyeOffIcon,
  ListPlus,
  FileTextIcon,
  FileTypeIcon,
  SigmaIcon
} from 'lucide-react';

export const NAV_ITEMS: NavItems[] = [
  {
    title: "Dashboard",
    path: "/",
    icon: GalleryVerticalEndIcon,
  },
  {
    title: "Chatbot",
    path: "/chatbot",
    icon: BotMessageSquareIcon,
  },
  {
    title: "Documents",
    path: "/documents",
    icon: FolderOpenIcon,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: SettingsIcon,
  }
];

export const MAX_FILE_SIZE = 10000000;


export const DOCUMENT_STATUSES = [
  {
    value: "INCONSISTENT",
    label: "Inconsistent",
    style: "warning",
    action: "Embed",
    actionMessage: "This document is incorrectly embedded. This action will re-embed the document. Are you sure?",
    groupActionMessage: "The selected documents are incorrectly embedded. This action will re-embed them. Documents that are already embedded correctly won't be affected. Are you sure?",
    actionIcon: SigmaIcon
  },
  {
    value: "CONCEALED",
    label: "Concealed",
    style: "disabled",
    action: "Enable",
    actionMessage: "This action will enable this document. The chatbot will be able to answer question about it. Are you sure?",
    groupActionMessage: "This action will enable the selected documents. Documents that are already enabled correctly won't be affected. Are you sure?",
    actionIcon: ListPlus
  },
  {
    value: "ENABLED",
    label: "Enabled",
    style: "successful",
    action: "Conceal",
    actionMessage: "This action will conceal this document. The chatbot won't be able to answer question about it. Are you sure?",
    groupActionMessage: "This action will conceal the selected documents. Documents that are already concealed correctly won't be affected. Are you sure?",
    actionIcon: EyeOffIcon
  },
  {
    value: "NOT_EMBEDDED",
    label: "Not Embedded",
    style: "error",
    action: "Embed",
    actionMessage: "This action will embed this document. Are you sure?",
    groupActionMessage: "This action will embed the selected documents. Documents that are already embedded correctly won't be affected. Are you sure?",
    actionIcon: SigmaIcon
  },
]

export const ALLOWED_FILE_TYPES = [
  {
    value: "PDF",
    type: "application/pdf",
    label: "PDF",
    action: "View content",
    icon: FileTextIcon,
  },
  {
    value: "DOCX",
    type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    label: "DOCX",
    action: "Download",
    icon: FileTypeIcon,
  },
]
