'use client';

import React from 'react';

import Link from 'next/link';
import { useSelectedLayoutSegment } from 'next/navigation';

import useScroll from '@/hooks/use-scroll';
import { cn } from '@/lib/utils';
import { Separator } from '@radix-ui/react-dropdown-menu';

type HeaderProps = {
  title?: string;
};

export default function Header({ title = "" }: HeaderProps) {
  const scrolled = useScroll(5);
  const selectedLayout = useSelectedLayoutSegment();

  return (
    <>
      <div className="h-[52px] sticky flex items-center px-4 top-0 z-50 w-full box-content border-b-[1px] bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <span className="font-bold text-xl flex">{title}</span>
      </div>
    </>
  );
};
