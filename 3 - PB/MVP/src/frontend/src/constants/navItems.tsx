import { NavItem } from '@/types/navItem';
import { FolderOpenIcon, LayoutDashboardIcon, MessageSquareTextIcon, SettingsIcon } from 'lucide-react';

export const NAV_ITEMS: NavItem[] = [
  {
    title: "Dashboard",
    path: "/",
    icon: LayoutDashboardIcon,
  },
  {
    title: "Chatbot",
    path: "/chatbot",
    icon: MessageSquareTextIcon,
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