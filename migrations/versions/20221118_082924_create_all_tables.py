"""Create all tables

Revision ID: 35d7d78d4a48
Revises: 
Create Date: 2022-11-18 08:29:24.659322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35d7d78d4a48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amenities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('alias', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('alias', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('profile_pic', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('listings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=5000), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('max_guests', sa.Integer(), nullable=False),
    sa.Column('bed', sa.Integer(), nullable=False),
    sa.Column('bath', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=225), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('startdate', sa.Date(), nullable=False),
    sa.Column('enddate', sa.Date(), nullable=False),
    sa.Column('created_at', sa.String(length=225), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('listing_amenities',
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.Column('amenity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amenity_id'], ['amenities.id'], ),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('listing_id', 'amenity_id')
    )
    op.create_table('listing_types',
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.PrimaryKeyConstraint('listing_id', 'type_id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.Column('review_body', sa.String(length=500), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('clean', sa.Integer(), nullable=False),
    sa.Column('comm', sa.Integer(), nullable=False),
    sa.Column('check', sa.Integer(), nullable=False),
    sa.Column('acc', sa.Integer(), nullable=False),
    sa.Column('loc', sa.Integer(), nullable=False),
    sa.Column('val', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=225), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlist_listings',
    sa.Column('wishlist_id', sa.Integer(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.ForeignKeyConstraint(['wishlist_id'], ['wishlists.id'], ),
    sa.PrimaryKeyConstraint('wishlist_id', 'listing_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlist_listings')
    op.drop_table('reviews')
    op.drop_table('listing_types')
    op.drop_table('listing_amenities')
    op.drop_table('images')
    op.drop_table('bookings')
    op.drop_table('wishlists')
    op.drop_table('listings')
    op.drop_table('users')
    op.drop_table('types')
    op.drop_table('amenities')
    # ### end Alembic commands ###
