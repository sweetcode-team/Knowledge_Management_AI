import { NavItems } from '@/types/types';
import {
  BotMessageSquareIcon,
  FolderOpenIcon,
  GalleryVerticalEndIcon,
  SettingsIcon
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