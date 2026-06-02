'use client'

import Image from 'next/image'
import Link from 'next/link'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card'
import Button from '@/components/ui/Button'
import { formatDate, formatTime, formatPrice } from '@/lib/utils'

const upcomingCourses = [
  {
    id: '1',
    title: 'Traditional Matcha Ceremony',
    titleEn: 'Traditional Matcha Ceremony',
    description: 'เรียนรู้การชงมัทฉะแบบดั้งเดิมและพิธีกรรมชาญี่ปุ่น',
    descriptionEn: 'Learn traditional matcha preparation and Japanese tea ceremony',
    instructor: 'Sensei Yamamoto',
    duration: 120, // minutes
    maxParticipants: 8,
    currentParticipants: 5,
    price: 1999,
    image: '/images/matcha-ceremony-class.jpg',
    startDateTime: new Date('2024-02-15T14:00:00'),
    endDateTime: new Date('2024-02-15T16:00:00'),
    level: 'Beginner',
    tags: ['Matcha', 'Ceremony', 'Traditional']
  },
  {
    id: '2',
    title: 'Sencha Brewing Masterclass',
    titleEn: 'Sencha Brewing Masterclass',
    description: 'เทคนิคการชงเซนฉะระดับมืออาชีพ',
    descriptionEn: 'Professional sencha brewing techniques',
    instructor: 'Master Tanaka',
    duration: 90,
    maxParticipants: 12,
    currentParticipants: 8,
    price: 1499,
    image: '/images/sencha-brewing-class.jpg',
    startDateTime: new Date('2024-02-18T10:00:00'),
    endDateTime: new Date('2024-02-18T11:30:00'),
    level: 'Intermediate',
    tags: ['Sencha', 'Brewing', 'Technique']
  },
  {
    id: '3',
    title: 'Tea Tasting & Pairing Workshop',
    titleEn: 'Tea Tasting & Pairing Workshop',
    description: 'การชิมชาและการจับคู่กับขนมญี่ปุ่น',
    descriptionEn: 'Tea tasting and pairing with Japanese sweets',
    instructor: 'Chef Sato',
    duration: 150,
    maxParticipants: 16,
    currentParticipants: 12,
    price: 2499,
    image: '/images/tea-tasting-workshop.jpg',
    startDateTime: new Date('2024-02-22T13:00:00'),
    endDateTime: new Date('2024-02-22T15:30:00'),
    level: 'All Levels',
    tags: ['Tasting', 'Pairing', 'Culture']
  }
]

const features = [
  {
    icon: (
      <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
      </svg>
    ),
    title: 'Expert Instructors',
    titleTh: 'ผู้สอนผู้เชี่ยวชาญ',
    description: 'Learn from certified tea masters with decades of experience'
  },
  {
    icon: (
      <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
      </svg>
    ),
    title: 'Small Groups',
    titleTh: 'กลุ่มเล็ก',
    description: 'Intimate classes with maximum 16 participants for personalized attention'
  },
  {
    icon: (
      <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0V6a2 2 0 00-2 2H8a2 2 0 00-2-2V6m8 0H8m0 0v-.5A1.5 1.5 0 016.5 4h11A1.5 1.5 0 0119 5.5V6" />
      </svg>
    ),
    title: 'Premium Materials',
    titleTh: 'อุปกรณ์พรีเมี่ยม',
    description: 'All tea and traditional utensils provided for authentic experience'
  },
  {
    icon: (
      <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
      </svg>
    ),
    title: 'Certification',
    titleTh: 'ใบรับรอง',
    description: 'Receive official certificate upon completion of each course'
  }
]

export default function CoursePreview() {
  return (
    <section className="py-16 lg:py-24 bg-white">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center bg-tea-gold bg-opacity-20 text-tea-brown px-4 py-2 rounded-full text-sm font-medium mb-6">
            <span className="w-2 h-2 bg-tea-gold rounded-full mr-2"></span>
            คอร์สเรียน • Tea Ceremony Classes
          </div>
          
          <h2 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-4">
            Master the Art of Tea
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
            เรียนรู้ศิลปะการชงชาญี่ปุ่นแบบดั้งเดิมจากผู้เชี่ยวชาญ พร้อมใบรับรองที่ได้รับการยอมรับ
          </p>

          {/* Features */}
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
            {features.map((feature, index) => (
              <div key={index} className="text-center">
                <div className="inline-flex items-center justify-center w-16 h-16 bg-hibi-100 text-hibi-600 rounded-full mb-4">
                  {feature.icon}
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600 text-sm">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Upcoming Courses */}
        <div className="mb-16">
          <h3 className="text-2xl font-bold text-gray-900 mb-8 text-center">
            Upcoming Classes
          </h3>
          
          <div className="grid lg:grid-cols-3 gap-8">
            {upcomingCourses.map((course) => (
              <Card key={course.id} variant="default" className="group overflow-hidden">
                <div className="relative aspect-video overflow-hidden rounded-t-lg">
                  <Image
                    src={course.image}
                    alt={course.title}
                    fill
                    className="object-cover group-hover:scale-110 transition-transform duration-500"
                  />
                  
                  {/* Level Badge */}
                  <div className="absolute top-3 left-3">
                    <span className="bg-hibi-500 text-white px-2 py-1 rounded text-sm font-medium">
                      {course.level}
                    </span>
                  </div>

                  {/* Price Badge */}
                  <div className="absolute top-3 right-3">
                    <span className="bg-white text-hibi-600 px-2 py-1 rounded text-sm font-bold">
                      {formatPrice(course.price)}
                    </span>
                  </div>
                </div>

                <CardHeader>
                  <CardTitle className="text-xl mb-2">{course.title}</CardTitle>
                  <p className="text-gray-600 text-sm line-clamp-2">
                    {course.description}
                  </p>
                </CardHeader>

                <CardContent className="space-y-4">
                  {/* Course Details */}
                  <div className="space-y-2">
                    <div className="flex items-center text-sm text-gray-600">
                      <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      </svg>
                      Instructor: {course.instructor}
                    </div>
                    
                    <div className="flex items-center text-sm text-gray-600">
                      <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      {course.duration} minutes
                    </div>

                    <div className="flex items-center text-sm text-gray-600">
                      <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3a2 2 0 012-2h4a2 2 0 012 2v4m-6 4v10a2 2 0 002 2h4a2 2 0 002-2V11" />
                      </svg>
                      {formatDate(course.startDateTime)} at {formatTime(course.startDateTime)}
                    </div>

                    <div className="flex items-center text-sm">
                      <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                      </svg>
                      <span className={course.currentParticipants >= course.maxParticipants ? 'text-red-600' : 'text-hibi-600'}>
                        {course.currentParticipants}/{course.maxParticipants} participants
                      </span>
                    </div>
                  </div>

                  {/* Tags */}
                  <div className="flex flex-wrap gap-2">
                    {course.tags.map((tag, tagIndex) => (
                      <span 
                        key={tagIndex} 
                        className="bg-hibi-50 text-hibi-600 px-2 py-1 rounded text-xs font-medium"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>

                  {/* Progress Bar */}
                  <div className="space-y-1">
                    <div className="flex justify-between text-sm text-gray-600">
                      <span>Enrollment Progress</span>
                      <span>{Math.round((course.currentParticipants / course.maxParticipants) * 100)}%</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div 
                        className="bg-hibi-500 h-2 rounded-full transition-all duration-300"
                        style={{ width: `${(course.currentParticipants / course.maxParticipants) * 100}%` }}
                      />
                    </div>
                  </div>

                  {/* Book Button */}
                  <Button 
                    className="w-full" 
                    disabled={course.currentParticipants >= course.maxParticipants}
                  >
                    {course.currentParticipants >= course.maxParticipants ? 'Fully Booked' : 'Book Now'}
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>

        {/* CTA Section */}
        <div className="text-center bg-gradient-to-r from-hibi-500 to-hibi-600 rounded-2xl p-12 text-white">
          <h3 className="text-3xl font-bold mb-4">
            Ready to Begin Your Tea Journey?
          </h3>
          <p className="text-xl mb-8 opacity-90">
            เริ่มต้นการเดินทางสู่โลกของชาญี่ปุ่นกับเรา
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/courses">
              <Button variant="outline" size="lg" className="bg-white text-hibi-600 border-white hover:bg-hibi-50">
                View All Courses
              </Button>
            </Link>
            <Link href="/contact">
              <Button variant="ghost" size="lg" className="text-white hover:bg-white hover:bg-opacity-10">
                Contact Us
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  )
}